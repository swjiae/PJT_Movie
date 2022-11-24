<template>
  <div>
    <nav>
      <hr>
      <router-link :to="{ name: 'MainView' }">Main</router-link>
      <hr>
    </nav>
    <div class="clearfix d-flex d-md-block flex-items-center mb-4 mb-md-0">
    <div class="position-relative d-inline-block col-2 col-md-12 mr-3 mr-md-0 flex-shrink-0" style="z-index:4;">
        <img style="height:auto;" alt="" width="260" height="260" class="avatar avatar-user width-full border color-bg-default" :src="uploadImg">
        <div class="vcard-names-container float-left js-profile-editable-names col-12 py-3 js-sticky js-user-profile-sticky-fields" data-original-top="0px" style="position: sticky;">
          <h1 class="vcard-names ">
            <span class="p-name vcard-fullname d-block overflow-hidden" itemprop="name">
              <h1>{{ getUser.nickname }}</h1>
            </span>
            <span class="p-nickname vcard-username d-block" itemprop="additionalName">
              <h5>{{ getUser.email }}</h5>
            </span>
          </h1>
        </div>
      
  <div class="user-status-container position-relative hide-sm hide-md">
    
    <div class="f5 js-user-status-context user-status-circle-badge-container user-status-editable" data-url="/users/status?circle=1&amp;compact=0&amp;link_mentions=1&amp;truncate=0">
      
<div class="js-user-status-container user-status-circle-badge d-inline-block lh-condensed-ultra p-2" data-team-hovercards-enabled="">
  <details class="js-user-status-details details-reset details-overlay details-overlay-dark">
    <summary class="btn-link btn-block Link--secondary no-underline js-toggle-user-status-edit toggle-user-status-edit">
      <div class="d-flex flex-items-center flex-items-stretch">
        <div class="
           ws-normal
           user-status-message-wrapper f6 min-width-0">
          <div class="css-truncate css-truncate-target width-fit color-fg-default">
              <span class="color-fg-muted">My Favorite Ganre</span>
          </div>
        </div>
      </div>
    </summary>
    <details-dialog class="rounded-2 anim-fade-in fast Box Box--overlay overflow-visible" role="dialog" aria-label="Edit status" tabindex="-1" aria-modal="true">
      
<form class="position-relative flex-auto js-user-status-form" data-turbo="false" action="/users/status?circle=1&amp;compact=0&amp;link_mentions=1&amp;truncate=0" accept-charset="UTF-8" method="post"><input type="hidden" name="_method" value="put" autocomplete="off"><input type="hidden" name="authenticity_token" value="MsU-AvQGHcuriI62uR9lTRbkAVfGJ3uZnv8Xlxw1yB1eKpG_8Z2rjs_p4TN_DPSfrb-y7PZqsXz250UtEaKrbQ">
  <input type="hidden" name="emoji" class="js-user-status-emoji-field" value="">
  <input type="hidden" name="organization_id" class="js-user-status-org-id-field" value="">
  <div class="px-3 py-2 color-fg-default">
    <div class="js-characters-remaining-container position-relative mt-2">
      <div class="input-group d-table form-group my-0 js-user-status-form-group">
      </div>
    </div>
    <include-fragment loading="lazy" src="/users/status/emoji"></include-fragment>
    <div class="overflow-auto ml-n3 mr-n3 px-3 border-bottom" style="max-height: 33vh">
      <div class="user-status-suggestions js-user-status-suggestions collapsed overflow-hidden">
        <div class="mx-3 mt-2 clearfix">
            <div class="float-left col-6">
                <button type="button" value=":palm_tree:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link Link--secondary no-underline js-predefined-user-status mb-1">
                  <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                    <g-emoji alias="palm_tree" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f334.png">🤣</g-emoji>
                  </div>
                  <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                    Comedy
                  </div>
                </button>
                <button type="button" value=":face_with_thermometer:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link Link--secondary no-underline js-predefined-user-status mb-1">
                  <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                    <g-emoji alias="face_with_thermometer" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f912.png">👻</g-emoji>
                  </div>
                  <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                    Horror
                  </div>
                </button>
            </div>
            <div class="float-left col-6">
                <button type="button" value=":house:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link Link--secondary no-underline js-predefined-user-status mb-1">
                  <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                    <g-emoji alias="house" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3e0.png">🏠</g-emoji>
                  </div>
                  <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                    Drama
                  </div>
                </button>
                <button type="button" value=":dart:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link Link--secondary no-underline js-predefined-user-status mb-1">
                  <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                    <g-emoji alias="dart" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3af.png">🤸</g-emoji>
                  </div>
                  <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                    Action
                  </div>
                </button>
            </div>
        </div>
      </div>
    </div>
  </div>
  
</form>
    </details-dialog>
  </details>
</div>
    </div>
  </div>
    </div>
  </div>
  <div>
    <!-- <ProfileUpdate/> -->
    <ProfileReviewList
      class="row d-flex"
    />
  </div>

  </div>
</template>

<script>
// import ProfileUpdate from '@/components/ProfileUpdate'
import ProfileReviewList from '@/components/ProfileReviewList'

export default {
    name: 'ProfileView',
    components: {
      // ProfileUpdate,
      ProfileReviewList,
    },
    computed: {
      getUser() {
        return this.$store.state.user
      },
      uploadImg() {
        if (!this.$store.state.user.profile_img) {
          return 'http://127.0.0.1:8000/media/profile_img/baekhyun.jpg'
        }
        return this.$store.state.user.profile_img
      }
    }
}
</script>

<style>
</style>